import streamlit as st
import pandas as pd
from TodoDB import *
import streamlit.components.v1 as stc

import plotly.express as px

HTML_BANNER = """
    <div style="background-color:#000080;padding:8px;border-radius:8px">
    <h1 style="color:#008080;text-align:center;">Todo Reminder App </h1>
    <p style="color:#008080;text-align:center;">Built with Streamlit</p>
    </div>
    """

def main():
    stc.html(HTML_BANNER)

    menu = ["Add Todo", "Lists", "Modify", "Remove", "About"]
    UserOption = st.sidebar.selectbox("Menu", menu)
    create_table()

    if UserOption == "Add Todo":
        st.subheader("Add Reminder")
        col1, col2 = st.beta_columns(2)

        with col1:
            Action = st.text_area("Task To Do")

        with col2:
            Reminder_Condition = st.selectbox("Status", ["Pending", "Ongoing", "Finished"])
            R_Expiration = st.date_input("Due Date")

        if st.button("Add Reminder"):
            add_data(Action, Reminder_Condition, R_Expiration)
            st.success("Added ::{} ::To Task".format(Action))


    elif UserOption == "Lists":
        # st.subheader("View Items")
        with st.beta_expander("View All"):
            result = view_all_data()
            # st.write(result)
            QuakeIt = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(QuakeIt)

        with st.beta_expander("Task Status"):
            task_df = QuakeIt['Status'].value_counts().to_frame()
            # st.dataframe(task_df)
            task_df = task_df.reset_index()
            st.dataframe(task_df)

            p1 = px.pie(task_df, names='index', values='Status')
            st.plotly_chart(p1, use_container_width=True)


    elif UserOption == "Modify":
        st.subheader("Modify Reminders")
        with st.beta_expander("Current Data"):
            result = view_all_data()
            # st.write(result)
            QuakeIt = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(QuakeIt)

        list_of_tasks = [i[0] for i in view_all_task_names()]
        selected_task = st.selectbox("Task", list_of_tasks)
        task_result = get_task(selected_task)
        # st.write(task_result)

        if task_result:
            task = task_result[0][0]
            Reminder_Condition = task_result[0][1]
            R_Expiration = task_result[0][2]

            col1, col2 = st.beta_columns(2)

            with col1:
                new_task = st.text_area("Task To Do", task)

            with col2:
                new_task_status = st.selectbox(Reminder_Condition, ["Pending", "Ongoing", "Finished"])
                new_task_due_date = st.date_input(R_Expiration)

            if st.button("Modify Reminder"):
                edit_task_data(new_task, new_task_status, new_task_due_date, task, Reminder_Condition, R_Expiration)
                st.success("Modified ::{} ::To {}".format(task, new_task))

            with st.beta_expander("View Modified Data"):
                result = view_all_data()
                # st.write(result)
                QuakeIt = pd.DataFrame(result, columns=["Task", "Status", "Date"])
                st.dataframe(QuakeIt)


    elif UserOption == "Remove":
        st.subheader("Remove")
        with st.beta_expander("View Data"):
            result = view_all_data()
            # st.write(result)
            QuakeIt = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(QuakeIt)

        unique_list = [i[0] for i in view_all_task_names()]
        delete_by_task_name = st.selectbox("Select Reminders", unique_list)
        if st.button("Remove"):
            delete_data(delete_by_task_name)
            st.warning("Removed: '{}'".format(delete_by_task_name))

        with st.beta_expander("Modified Data"):
            result = view_all_data()
            # st.write(result)
            QuakeIt = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(QuakeIt)

    else:
        st.subheader("About ToDo List App")
        st.info("Powered by Streamlit")
        st.info("All Rights Reserved 2022")
        st.text("Laziness is nothing more than the habit of resting before you get tired)")



if __name__ == '__main__':
    main()