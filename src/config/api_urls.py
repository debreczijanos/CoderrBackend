from django.urls import include, path

urlpatterns = [
    path("", include("apps.core.urls")),
    path("", include("apps.accounts.urls")),
    path("", include("apps.profiles.urls")),
    path("", include("apps.projects.urls")),
    path("", include("apps.proposals.urls")),
    path("", include("apps.contracts.urls")),
    path("", include("apps.payments.urls")),
    path("", include("apps.reviews.urls")),
    path("", include("apps.offers.urls")),
    path("", include("apps.offerdetails.urls")),
    path("", include("apps.orders.urls")),
]
