import sublime
import sublime_plugin
from contextlib import contextmanager
import os
import json

class ProjectDataManager():
    def __init__(self, view):
        self.view = view

    def get_project_folder(self) -> str:
        project_folders = self.view.window().folders()
        if not project_folders:
            print("no project folder found")
            raise Exception("No project folder found. Please open a project.")
        return os.path.realpath(project_folders[0])

    def ensure_project_file(self):
        folder = self.get_project_folder()
        if folder is None:
            print("no project folder found")
            sublime.error_message("No project folder found. Please open a project.")
            return None

        project_file = os.path.join(folder, os.path.basename(folder) + '.sublime-project')
        if not os.path.exists(project_file):
            project_data = self.ensure_project_data_fields({'folders': [{'path': folder}]})
            self.view.window().set_project_data(project_data)
            with open(project_file, 'w', encoding='utf-8') as f:
                json.dump(project_data, f, indent=4)
        return project_file

    @contextmanager
    def project_data_context(self):
        project_file = self.ensure_project_file()
        if not project_file:
            project_data = self.ensure_project_data_fields(self.view.window().project_data())
        else:
            with open(project_file, 'r', encoding='utf-8') as f:
                project_data = self.ensure_project_data_fields(json.load(f))

        print('project data', project_data)

        self.view.window().set_project_data(project_data)

        try:
            yield project_data
        finally:
            project_data = self.ensure_project_data_fields(project_data)
            self.view.window().set_project_data(project_data)

            project_file_name = self.ensure_project_file()
            if not project_file_name:
                return

            with open(project_file_name, 'w', encoding='utf-8') as f:
                json.dump(project_data, f, indent=4)

    def ensure_project_data_fields(self, project_data):
        if not project_data:
            project_data = {}
        if 'file_browser' not in project_data:
            project_data['file_browser'] = {}
        if 'marked_files' not in project_data['file_browser']:
            project_data['marked_files'] = []
        return project_data
