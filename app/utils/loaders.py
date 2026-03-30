import os

def load_documents(data_path):
    documents = []

    for file in os.listdir(data_path):
        file_path = os.path.join(data_path, file)

        with open(file_path, "r") as f:
            text = f.read()

        documents.append({
            "content": text,
            "source": file
        })

    return documents


# # ✅ Test input
# data_path = "data/raw"
# result = load_documents(data_path)
# print (result)

