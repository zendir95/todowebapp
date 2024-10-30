import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append((new_todo + "\n"))
    functions.write_todos(todos)
    st.session_state["new_todo"]= ""

st.title("<< My Todo App >>")

st.text_input(label="Enter a Todo", placeholder="Write something to...do",
              on_change=add_todo, key="new_todo")

st.subheader("Todo list: ", divider="grey")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}.{todo}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{index}.{todo}"]
        st.rerun()



# st.session_state
# pip freeze > requirements.txt <<- genera file requirements.txt utile al server per conoscere tutti le library dependencies