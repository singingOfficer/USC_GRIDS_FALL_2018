
# coding: utf-8

# In[10]:


get_ipython().system('jupyter nbconvert --to script config_template.ipynb')
import tensorflow as tf


# In[11]:


a = tf.constant(2)
b = tf.constant(3)
x = a*b 
with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graphs', sess.graph)
    print(sess.run(x))
    
writer.close()

