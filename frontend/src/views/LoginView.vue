<template>
  <my-message
    @closeMessage="closeMessage"
    v-if="showMessages"
    :messages="messages"
  />
  <LoginForm @loginUser="loginUser" style="max-width: 35rem" />
</template>

<script>
import LoginForm from "@/components/LoginForm.vue";
import axios from "axios";
export default {
  data() {
    return {
      messages: [],
      showMessages: false,
    };
  },
  components: {
    LoginForm,
  },
  methods: {
    loginUser(login_form) {
      // Clear messages
      this.closeMessage();

      // Check empty fields
      for (const key in login_form) {
        if (!login_form[key]) {
          this.messages.push("Some fields are empty.");
          this.showMessages = true;
          return;
        }
      }

      // Send request
      axios
        .post("/api/v1/token/login/", login_form)
        // Handle success
        .then((res) => {
          const token = res.data.auth_token;

          if (token) {
            this.$store.commit("setToken", token);
            localStorage.setItem("token", token);
            axios.defaults.headers.common["Authorization"] = "Token " + token;

            this.$router.push("/notes");
          }
        })
        // Handle errors
        .catch((error) => {
          this.messages.push(error.message);
          for (const key in error.response.data) {
            for (var i = 0; i < error.response.data[key].length; i++) {
              this.messages.push(error.response.data[key][i]);
            }
          }
          this.showMessages = true;
        });
    },
    closeMessage() {
      this.messages = [];
      this.showMessages = false;
    },
  },
};
</script>

<style scoped></style>
