import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Library Management", layout="wide")
st.title("📚 Library Management System")

tabs = st.tabs(["📘 Books", "🎓 Issue Book", "📄 Transactions"])


with tabs[0]:
    st.subheader("Books Available")

    # Fetch books
    res = requests.get(f"{BASE_URL}/books")
    books = res.json()

    st.data_editor(books, key="books_editor")

    st.divider()

    st.subheader("Add New Book")
    book_name = st.text_input("Book Name")

    if st.button("Add Book", type="primary"):
        if book_name:
            requests.post(f"{BASE_URL}/books", params={"book_name": book_name})
            st.success("Book added successfully")
            st.rerun()


with tabs[1]:
    st.subheader("Issue Book to Student")

    book_id = st.text_input("Book ID")
    student_id = st.text_input("Student ID")

    if st.button("Issue Book", type="primary"):
        if book_id and student_id:
            res = requests.post(
                f"{BASE_URL}/issue-book",
                params={
                    "book_id": int(book_id),
                    "student_id": int(student_id)
                }
            )
            st.success(res.json()["message"])
            st.rerun()


with tabs[2]:
    st.subheader("Issued Books / Transactions")

    res = requests.get(f"{BASE_URL}/transactions")
    transactions = res.json()

    st.data_editor(transactions, key="transactions_editor")

    st.divider()

    st.subheader("Collect Book")
    txn_id = st.text_input("Transaction ID")

    if st.button("Collect Book", type="primary"):
        if txn_id:
            requests.put(f"{BASE_URL}/collect-book/{txn_id}")
            st.success("Book collected successfully")
            st.rerun()
