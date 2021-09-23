import ast
import csv
import os


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as myfile:
                reader = csv.DictReader(myfile)
                return list(reader)
        else:
            return []

    # when we edit a file we want to overwrite it, so we need to tell the file that opens in mode="w"
    def add_to_file(self, new_value, mode="a"):
        if isinstance(new_value, dict):
            fields = new_value.keys()
            new_value = [new_value]
        elif isinstance(new_value, list):
            fields = new_value[0].keys()
        with open(self.file_path, mode) as myfile:
            writer = csv.DictWriter(myfile, fieldnames=fields)
            if myfile.tell() == 0:
                writer.writeheader()
            writer.writerows(new_value)

    def edit_row(self, updated_dict):
        all_rows = self.read_file()
        final_rows = []
        for row in all_rows:
            information = ast.literal_eval(row["information"])
            if information["address"]["postal_code"] == updated_dict["information"]["address"]["postal_code"]:
                row = updated_dict
            final_rows.append(row)
        self.add_to_file(final_rows, mode="w")

    def delete_row(self, dict_to_delete):
        all_rows = self.read_file()
        final_rows = []
        for row in all_rows:
            information = ast.literal_eval(row["information"])
            if information["address"]["postal_code"] == dict_to_delete["information"]["address"]["postal_code"]:
                continue
            final_rows.append(row)
        self.add_to_file(final_rows, mode="w")
