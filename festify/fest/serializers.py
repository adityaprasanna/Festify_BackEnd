from rest_framework_mongoengine import serializers

from festify.accountDetails.models import AccountDetails
from festify.accountDetails.serializers import AccountDetailsSerializer
from festify.coordinator.models import Coordinator
from festify.coordinator.serializers import CoordinatorSerializer
from festify.event.models import Event
from festify.fest.models import Fest
from festify.fest.models import FestV2
from festify.event.serializers import EventSerializer
from festify.file.serializers import FileSerializer
from festify.organization.models import Organization
from festify.organization.serializers import OrganizationSerializer
from festify.sponsor.models import Sponsor
from festify.sponsor.serializers import SponsorSerializer


class FestSerializer(serializers.DocumentSerializer):
    fest_events = EventSerializer
    fest_image = FileSerializer
    fest_sponsor = SponsorSerializer
    fest_coordinator = CoordinatorSerializer
    fest_organizer = OrganizationSerializer

    class Meta:
        model = Fest
        fields = "__all__"


def delete_coordinators(coordinators):
    for coordinator in coordinators:
        Coordinator(id=coordinator).delete()
        
        
def delete_events(events):
    for event in events:
        Event(id=event).delete()


def delete_sponsors(sponsors):
    for sponsor in sponsors:
        Sponsor(id=sponsor).delete()


class EventSerializerV2(serializers.DocumentSerializer):
    # event_coordinator = serializers.serializers.ListField(required=False)
    event_coordinator = serializers.serializers.CharField(required=False)
    event_images = serializers.serializers.ListField(required=False)

    class Meta:
        model = Event
        fields = "__all__"
        
        
class SponsorSerializerV2(serializers.DocumentSerializer):
    sponsor_picture = serializers.serializers.ListField(required=False)
    
    class Meta:
        model = Sponsor
        fields = "__all__"
        
        
class OrganizationSerializerV2(serializers.DocumentSerializer):
    org_image = serializers.serializers.ListField(required=False)
    
    class Meta:
        model = Organization
        fields = "__all__"
        
        
def dbref_to_string(data, typ):
    data = str(data)
    data = data.replace("DBRef('"+typ+"', ObjectId(", "")
    data = data.replace("'", "")
    data = data.replace(")", "")
    
    data.replace("[", "")
    data.replace("]", "")
    return data


class FestSerializerV2(serializers.DocumentSerializer):
    fest_events = EventSerializerV2(many=True)
    fest_image = serializers.serializers.ListField(required=False)
    fest_sponsor = SponsorSerializerV2(many=True)
    fest_coordinator = CoordinatorSerializer(many=True)
    fest_account_details = AccountDetailsSerializer(many=True)
    fest_organizer = serializers.serializers.CharField(required=False)
    
    class Meta:
        model = FestV2
        fields = "__all__"

    def create(self, validated_data):
        # print(dict(validated_data["fest_events"][0]))
        created_fest_coordinators = []
        created_event_coordinators = []
        created_account_details = []
        created_events = []
        created_sponsors = []
        
        # 0. Create Account Details
        try:
            for account_detail in validated_data["fest_account_details"]:
                account_detail_to_create = AccountDetailsSerializer(data=account_detail)
                account_detail_to_create.is_valid(raise_exception=True)
                a = AccountDetails.objects.create(**account_detail)
                created_account_details.append(a.id)
        except Exception as e:
            raise Exception(e)
        
        # 1. Create fest Coordinator
        try:
            for coordinator in validated_data["fest_coordinator"]:
                coordinator_to_create = CoordinatorSerializer(data=coordinator)
                coordinator_to_create.is_valid(raise_exception=True)
                c = Coordinator.objects.create(**coordinator)
                created_fest_coordinators.append(c.id)
        except Exception as e:
            raise Exception(e)

        # 2. Create Organizer
        # organizer = dict(validated_data["fest_organizer"])
        # organizer["org_coordinator"] = created_fest_coordinators
        #
        # organizer["org_image"] = [dbref_to_string(organizer["org_image"])]
        #
        # try:
        #     organizer_to_create = OrganizationSerializerV2(data=organizer)
        #     organizer_to_create.is_valid(raise_exception=True)
        #     created_organizer = Organization.objects.create(**organizer)
        # except Exception as e:
        #     print(123123)
        #
        #     delete_coordinators(created_fest_coordinators)
        #     raise Exception(e)

        # 3. Create Events
        try:
            for event in validated_data["fest_events"]:
                current_event_coordinator_list = []
                if "event_coordinator" in event.keys() and type(event["event_coordinator"]) is list:
                    for coordinator in event["event_coordinator"]:
                        coordinator_to_create = CoordinatorSerializer(data=coordinator)
                        coordinator_to_create.is_valid(raise_exception=True)
                        c = Coordinator.objects.create(**coordinator)
                        created_event_coordinators.append(c.id)
                        current_event_coordinator_list.append(str(c.id))
        
                    event["event_coordinator"] = current_event_coordinator_list
    
                event_images_list = []
                for images in event["event_images"]:
                    event_images_list.append(dbref_to_string(images, 'file'))
    
                event["event_images"] = event_images_list
                event_to_create = EventSerializer(data=event)
                event_to_create.is_valid(raise_exception=True)
                e = Event.objects.create(**event)
                created_events.append(e.id)
                
        except Exception as e:
            delete_coordinators(created_fest_coordinators)
            delete_coordinators(created_event_coordinators)
            raise Exception(e)

        # 4. Create Sponsors
        try:
            for sponsor in validated_data["fest_sponsor"]:
                sponsor_images_list = []
                for images in sponsor["sponsor_picture"]:
                    sponsor_images_list.append(dbref_to_string(images, 'file'))

                sponsor["sponsor_picture"] = sponsor_images_list
                sponsor_to_create = SponsorSerializerV2(data=sponsor)
                sponsor_to_create.is_valid(raise_exception=True)
                s = Sponsor.objects.create(**sponsor)
                created_sponsors.append(s.id)
        except Exception as e:
            delete_coordinators(created_fest_coordinators)
            delete_coordinators(created_event_coordinators)
            delete_events(created_events)
            raise Exception(e)

        # 5. Create a fest now
        try:
            fest_images_list = []
            for images in validated_data["fest_image"]:
                fest_images_list.append(dbref_to_string(images, 'file'))
                
            validated_data["fest_image"] = fest_images_list
            validated_data["fest_organizer"] = dbref_to_string(validated_data["fest_organizer"], 'organization')
            fest_to_create = FestSerializerV2(data=validated_data)
            fest_to_create.is_valid(raise_exception=True)
            fest_created = FestV2.objects.create(**validated_data)

        except Exception as e:
            print(e)
            delete_coordinators(created_fest_coordinators)
            delete_coordinators(created_event_coordinators)
            delete_events(created_events)
            delete_sponsors(created_sponsors)
            raise Exception(e)

        return fest_created
