# GitLens -- Git supercharged
# Author : rizkyadiryanto14
# Email  : adiryantorizky140820@gmail.com

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("profile", views.Profile, name="profile"),
    path("dispute", views.DisputeView, name="dispute"),
    path(
        "your-company-information",
        views.YourCompanyInformation,
        name="your-company-information",
    ),
    path(
        "add-business-tradelines",
        views.AddBusinessTradelines,
        name="add-business-tradelines",
    ),
    path(
        "update-company-information",
        views.UpdateCompanyInformation,
        name="update-company-information",
    ),
    path(
        "business-credit-reports",
        views.BusinessCreditReports,
        name="business-credit-reports",
    ),
    path(
        "current-business-tradelines",
        views.CurrentBusinessTradelines,
        name="current-business-tradelines",
    ),
]
