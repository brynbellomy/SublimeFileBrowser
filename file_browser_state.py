# import sublime
# import os
# from .project_data import ProjectDataManager

# def plugin_loaded():
#     state = FileBrowserState(sublime.active_window())
#     state.set_marked_files(sublime.active_window(), [])

# class FileBrowserState(ProjectDataManager):
#     def __init__(self, view):
#         ProjectDataManager.__init__(self, view)
#         self.marked_files = {}

#     def set_marked_files(self, files):
#         print('SET MARKED FILES', files)
#         with self.project_data_context() as project_data:
#             window_id = self.view.window().id()
#             self.marked_files[window_id] = files

#             # Save marked files to project data
#             project_data = self.view.window().project_data()
#             if project_data is None:
#                 project_data = {}

#             project_data['file_browser']['marked_files'] = files or []

#     def get_marked_files(self, window_id):
#         # First, try to get marked files from memory
#         print('GET MARKED FILES')
#         files = self.marked_files.get(window_id, [])

#         # If not found in memory, try to get from project data
#         if not files:
#             window = sublime.active_window()
#             project_data = window.project_data()
#             if project_data and 'file_browser_marked_files' in project_data:
#                 files = project_data['file_browser_marked_files']
#                 self.marked_files[window_id] = files  # Cache in memory

#         return files


