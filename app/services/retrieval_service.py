from app.services.vectorstore_service import get_vectorstore

def retrieve_documents(query,k =3):
    vectorstore = get_vectorstore()

    results = vectorstore.similarity_search(query,k=k)

    return results


    


