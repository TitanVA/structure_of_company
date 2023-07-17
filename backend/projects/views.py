from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from projects.models import Project
from projects.serializers import ProjectsListSerializer, ProjectsDetailSerializer


# class DynamicSerializerMixin():
#     def get_serializer_class(self):
#         if self.action == "list":
#             return ProjectsListSerializer
#         return ProjectsDetailSerializer


class ProjectsVewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectsListSerializer
        return ProjectsDetailSerializer


