import sublime, sublime_plugin, os, platform

class Cjump_Utils:
    def is_windows_system(self):
        return platform.system() == 'Windows'

    def isdir(self,path):
        return os.path.isdir(path)

    def close_and_reopen(self,window,file_path):
        print(file_path)
        window.run_command('close_file')
        window.open_file(file_path,0)

utils = Cjump_Utils()

class Cjump_next_fileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        split_char = '/'
        if utils.is_windows_system():
            split_char = '\\';
        file_path = self.view.file_name()
        if(file_path == None):
            return
        file_name = file_path[file_path.rindex(split_char)+1:]
        file_dir = file_path[:file_path.rindex(split_char)+1]
        found = False
        for files in os.listdir(file_dir):
            if(utils.isdir(file_dir+files)):
                continue
            if found:
                utils.close_and_reopen(self.view.window(),file_dir+files)
                break
            if files == file_name:
                found = True


class Cjump_previous_fileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        split_char = '/'
        if utils.is_windows_system():
            split_char = '\\';
        file_path = self.view.file_name()
        if(file_path == None):
            return
           
        file_name = file_path[file_path.rindex(split_char)+1:]
        file_dir = file_path[:file_path.rindex(split_char)+1]     
        found = False
        last_file = ""
        for files in os.listdir(file_dir):
            if(utils.isdir(file_dir+files)):
                continue
            if files == file_name:
                found = True
                break
            last_file = files

        if last_file != "":
            utils.close_and_reopen(self.view.window(),file_dir+last_file)