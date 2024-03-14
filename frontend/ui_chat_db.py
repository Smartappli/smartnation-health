import streamlit as st

<<<<<<< HEAD
import pathlib
import sys

from utils import make_footer

=======
# from streamlit_lottie import st_lottie
import pathlib
import sys

>>>>>>> a5a3db7 (Code added for Smart Nation AI)
ROOT_PATH = pathlib.Path(__file__).parent
ASSETS_PATH = ROOT_PATH / "assets"

BACKEND_PATH = ROOT_PATH.parent / "src"
sys.path.append(str(BACKEND_PATH))
<<<<<<< HEAD
import answer_questions  # noqa
=======
import answer_questions
>>>>>>> a5a3db7 (Code added for Smart Nation AI)


class Chatbot:
    def __init__(self):
<<<<<<< HEAD
        st.set_page_config(page_icon="💬", page_title="SmartNation")

        if "patient_id" not in st.session_state:
            st.session_state.patient_id = ""
=======
        try:
            st.set_page_config(page_icon="💬", page_title="SmartNation")
        except:
            pass
>>>>>>> a5a3db7 (Code added for Smart Nation AI)

        if "chat_ready" not in st.session_state:
            st.session_state["chat_ready"] = False

<<<<<<< HEAD
        if "disable_validate" not in st.session_state:
            st.session_state["disable_validate"] = False

        if "disable_new" not in st.session_state:
            st.session_state["disable_new"] = False
=======
        else:
            pass

        if "validate_id" not in st.session_state:
            st.session_state["validate_id"] = False
        else:
            pass

        if "new_id" not in st.session_state:
            st.session_state["new_id"] = False
        else:
            pass
>>>>>>> a5a3db7 (Code added for Smart Nation AI)

        if "start" not in st.session_state:
            st.session_state["start"] = True

        if "patient_id" not in st.session_state:
            st.session_state.text_input_value = ""

        if "messages" not in st.session_state:
            st.session_state["messages"] = [
                {"role": "assistant", "content": "Comment puis-je vous aider?"}
            ]

    def default_chatbot(self):
<<<<<<< HEAD
        st.title("Assistant virtuel de Vivalia")
        st.markdown(
            "Veuillez saisir l'ID patient et commencez à poser vos questions")
        # st.image(str(ASSETS_PATH / "default_view.png"))

    def create_chatbot(self):
        st.markdown(f"## Dossier patient:`{st.session_state.patient_id}`")
=======
        st.title("Chatbot assistant de Vivalia")
        st.markdown("Veuillez saisir l'ID patient et commencez à poser vos questions")
        st.image(str(ASSETS_PATH / "default_view.png"))

        # st_lottie("https://lottie.host/b542951f-9a58-4962-b803-7024c51306da/RwyQLtKCmZ.json", height=600, key='coding')

    def create_chatbot(self):
        st.markdown(f"## Vous êtes avec le patient avec le ID `{self.patient_id}`")
>>>>>>> a5a3db7 (Code added for Smart Nation AI)
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input():
<<<<<<< HEAD
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            with st.spinner("Writing..."):
                if st.session_state.patient_id:
                    response = {
                        "answer": answer_questions.answer_question(
                            st.session_state.patient_id, prompt
                        )
                    }
                else:
                    response = {
                        "answer": "Veuillez saisir l'ID du patient d'abord"}
=======
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            request = {
                "question": prompt,
                "chat_history": "",
                "patient_id": self.patient_id,
            }

            with st.spinner("Writing..."):
                if self.patient_id:
                    # response = self.dummy_response(request)
                    response = {
                        "answer": answer_questions.answer_question(
                            self.patient_id, prompt
                        )
                    }
                else:
                    response = {"answer": "Veuillez saisir l'ID du patient d'abord"}
>>>>>>> a5a3db7 (Code added for Smart Nation AI)

            msg = {"content": response["answer"], "role": "assistant"}
            st.session_state.messages.append(msg)

            st.chat_message("assistant").write(response["answer"])

<<<<<<< HEAD
    def send_question(self, question):
        with st.spinner("Writing..."):
            if st.session_state.patient_id:
                response = {
                    "answer": answer_questions.answer_question(
                        st.session_state.patient_id, question
=======
    def dummy_response(self, prompt):
        response = {"answer": "Ceci est la réponse de l'API"}

        return response

    def send_question(self, question):
        with st.spinner("Writing..."):
            request = {
                "question": question,
                "chat_history": "",
                "patient_id": self.patient_id,
            }

            if self.patient_id:
                response = {
                    "answer": answer_questions.answer_question(
                        self.patient_id, question
>>>>>>> a5a3db7 (Code added for Smart Nation AI)
                    )
                }

            else:
<<<<<<< HEAD
                response = {
                    "answer": "Veuillez saisir l'ID du patient d'abord"}
=======
                response = {"answer": "Veuillez saisir l'ID du patient d'abord"}
>>>>>>> a5a3db7 (Code added for Smart Nation AI)

        st.session_state.messages.append({"role": "user", "content": question})
        st.session_state.messages.append(
            {"role": "assistant", "content": response["answer"]}
        )

    def create_sidebar(self):
        st.sidebar.image(str(ASSETS_PATH / "logo_vivalia.svg"), width=200)
        st.sidebar.title("Discutez avec la base de données")
        st.sidebar.markdown(
            "Veuillez saisir l'ID patient et commencez à poser vos questions"
        )

        st.sidebar.divider()

<<<<<<< HEAD
        if (
            "bt_validate" in st.session_state
            and st.session_state["bt_validate"]
            and st.session_state.patient_id
        ):
            st.session_state.disable_validate = True
            st.session_state.disable_new = False
=======
        st.sidebar.header("Patient ID")

        self.patient_id_placeholder = st.sidebar.empty()
        self.patient_id = self.patient_id_placeholder.text_input(
            "Patient ID", label_visibility="hidden"
        )

        placeholder = st.sidebar.empty()

        if "bt_validate" in st.session_state and st.session_state["bt_validate"]:
            st.session_state.validate_id = True
            st.session_state.new_id = False
>>>>>>> a5a3db7 (Code added for Smart Nation AI)

        if "bt_new" in st.session_state and st.session_state["bt_new"]:
            st.session_state.messages = [
                {"role": "assistant", "content": "Comment puis-je vous aider?"}
            ]
<<<<<<< HEAD
            st.session_state.disable_new = True
            st.session_state.disable_validate = False
            st.session_state.chat_ready = False
        elif "bt_new" not in st.session_state:
            st.session_state.disable_new = True

        st.sidebar.header("Patient ID")

        self.patient_id_placeholder = st.sidebar.empty()
        st.session_state.patient_id = self.patient_id_placeholder.text_input(
            "Patient ID",
            label_visibility="hidden",
            disabled=st.session_state.disable_validate,
        )

        placeholder = st.sidebar.empty()

        col1, col2 = placeholder.columns(2)
        with col1:
            validate_id = st.sidebar.button(
                "Valider l'ID",
                disabled=st.session_state.disable_validate,
                key="bt_validate",
            )
        with col2:
            new_id = st.sidebar.button(
                "Changer de patient",
                disabled=st.session_state.disable_new,
                key="bt_new",
            )

        if validate_id or st.session_state.disable_validate:
            if st.session_state.patient_id:
                st.session_state.disable_validate = True
                st.session_state.disable_new = False
=======
            st.session_state.new_id = True
            st.session_state.validate_id = False
            st.session_state.chat_ready = False

        col1, col2 = placeholder.columns(2)
        with col1:
            print("st.session_state.validate_id: ", st.session_state.validate_id)
            validate_id = st.sidebar.button(
                "Valider l'ID", disabled=st.session_state.validate_id, key="bt_validate"
            )
        with col2:
            print("st.session_state.new_id: ", st.session_state.new_id)
            new_id = st.sidebar.button(
                "Nouveau ID", disabled=st.session_state.new_id, key="bt_new"
            )

        if validate_id or st.session_state.validate_id:
            if self.patient_id:
                st.session_state.validate_id = True
                st.session_state.new_id = False
>>>>>>> a5a3db7 (Code added for Smart Nation AI)
                st.session_state.chat_ready = True

                st.sidebar.divider()

                suggested_questions = [
<<<<<<< HEAD
                    "Quels sont les antécédents médicaux du patient?",
                    "Ce patient est-il diabétique?",
                    "Fournir des informations sur l'IMC et voir si le patient est en bonne santé",
=======
                    "Montre-moi les antécédents médicaux?",
                    "Ce patient est-il diabétique?",
                    "Fournir des informations sur l'IMC et voir si le patient est en bonne santé?",
>>>>>>> a5a3db7 (Code added for Smart Nation AI)
                ]

                st.sidebar.subheader("Questions suggérées")
                for question in suggested_questions:
                    if st.sidebar.button(question):
                        self.send_question(question)

<<<<<<< HEAD
        if new_id or st.session_state.disable_new:
            st.session_state.messages = [
                {"role": "assistant", "content": "En quoi puis-je vous aider?"}
            ]
            st.session_state.disable_new = True
            st.session_state.disable_validate = False
=======
        if new_id or st.session_state.new_id:
            st.session_state.messages = [
                {"role": "assistant", "content": "How can I help you?"}
            ]
            st.session_state.new_id = True
            st.session_state.validate_id = False
>>>>>>> a5a3db7 (Code added for Smart Nation AI)
            st.session_state.chat_ready = False

    def update_session(self):
        pass

    def run(self):
        self.create_sidebar()

        if st.session_state.chat_ready:
            self.create_chatbot()
        else:
            self.default_chatbot()
<<<<<<< HEAD
            make_footer(st, ASSETS_PATH, n_lines=2)
=======
>>>>>>> a5a3db7 (Code added for Smart Nation AI)


if __name__ == "__main__":
    app = Chatbot()
    app.run()
