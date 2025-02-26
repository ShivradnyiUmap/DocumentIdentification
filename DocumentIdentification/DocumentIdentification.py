#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[39]:


pip install chromadb


# In[40]:


import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection1 = client.create_collection(name="my_collection1")


# In[ ]:


collection1.add(
    documents=[
        "Diwali",
        "Christmas"
    ],
    ids = ['id1', 'id2']
)


# In[ ]:


all_docs = collection1.get()
all_docs


# In[ ]:


documents = collection1.get(ids=["id1"])
documents


# In[ ]:


results = collection1.query(
    query_texts=['Query is about Christmas Tree'],
    n_results=2
)
results


# In[ ]:


collection1.delete(ids=all_docs['ids'])
collection1.get()


# In[ ]:


collection1.add(
    documents=[
        "This document is about Christmas",
        "This document is about Diwali"
    ],
    ids=["id3", "id4"],
    metadatas=[
        {"url": "https://en.wikipedia.org/wiki/Diwali"},
        {"url": "https://en.wikipedia.org/wiki/Christmas"}
    ]
)


# In[ ]:


results = collection1.query(
    query_texts=["Would like to know about Lakshmipoojan"],
    n_results=2
)
results


# In[ ]:




