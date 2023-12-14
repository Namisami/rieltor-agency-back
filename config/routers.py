from rest_framework import routers
from esoft.views import ClientViewSet, AgentViewSet, ObjectTypeViewSet, ObjectViewSet, OfferViewSet, DemandViewSet, DealViewSet, DistrictViewSet

router = routers.DefaultRouter()

router.register('clients', ClientViewSet) 
router.register('agents', AgentViewSet) 
router.register('types', ObjectTypeViewSet) 
router.register('objects', ObjectViewSet) 
router.register('districts', DistrictViewSet) 
router.register('offers', OfferViewSet) 
router.register('needs', DemandViewSet) 
router.register('deals', DealViewSet)
