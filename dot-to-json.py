
# coding: utf-8

# In[6]:


from dot_tools import parse
with open ("8.dot", "r") as myfile:
    data=myfile.read()
    


# In[9]:


data = data.replace("Digraph","digraph")


# In[10]:


tree=parse(data)


# In[11]:


from dot_tools.dot_graph import SimpleGraph


# In[12]:


g = SimpleGraph.build(tree.kid('Graph'))


# In[13]:


constant = ' "id":"1", "fontcolor":"blue","shape":"plaintext","label":"Cluster ID: 1344\\nSpecific Mutation Type: Response time change\\nCost: 206331909\\nOverall Mutation Type: Originating_Cluster and_Response_Time_Change\\nCandidate originating clusters: \\n\\nAvg. response times: 42170 us ; 70959 us\\nStandard Deviations: 7580 us ; 13811 us\\nKS-Test2 P-value: 0.000\\nCluster likelihood: 0.0340 ; 0.0291\\nPercent makeup: 54 / 46\\nrequests: 7167 ; 6082" '


# In[16]:


import json

fo = open("8.json", "w+")
temp = json.dumps([{'id': k, 'label': v['label']} for k,v in g.nodes.items()], indent=4)
fixed = temp [1:]
fo.write('{  "nodes": [ \n\t{' + constant+'}'+'\n' + fixed+',' )
tmp = json.dumps([{'from': x, 'to': y,'color':"black" ,'label':"p:1.00\n   a: 8us / 8us\n   s: 2us / 2us" , 'time' : z,} for x,y,z in g.edges], indent=4)
fixedd = tmp [1:]
#print fixedd
fo.write(' \n"edges": [ \n\t' + fixedd)
fo.close()

