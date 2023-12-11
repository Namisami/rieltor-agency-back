from rest_framework import routers
from esoft.views import ClientViewSet, AgentViewSet, TypesViewSet, ObjectViewSet, OfferViewSet, NeedViewSet, DealViewSet

router = routers.DefaultRouter()

router.register('clients', ClientViewSet) 
router.register('agents', AgentViewSet) 
router.register('types', TypesViewSet) 
router.register('objects', ObjectViewSet) 
router.register('offers', OfferViewSet) 
router.register('needs', NeedViewSet) 
router.register('deals', DealViewSet)
