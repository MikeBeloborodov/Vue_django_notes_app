<template>
  <my-message
    @closeMessage="closeMessage"
    v-if="showMessages"
    :messages="messages"
  />
  <SignupForm @signupUser="signupUser" style="max-width: 35rem" />
</template>

<script>
import SignupForm from "@/components/SignupForm.vue";
import axios from "axios";
export default {
  data() {
    return {
      messages: [],
      showMessages: false,
    };
  },
  components: {
    SignupForm,
  },
  methods: {
    signupUser(user_form) {
      // Clear messages
      this.closeMessage();

      // Check passwords
      if (user_form.password1 != user_form.password2) {
        this.message.push("Passwords do not match.");
        this.showMessages = true;
      }

      // Check empty fields
      for (const key in user_form) {
        if (!user_form[key]) {
          this.messages.push("Some fields are empty.");
          this.showMessages = true;
          return;
        }
      }

      const form = {
        username: user_form.username,
        email: user_form.email,
        password: user_form.password1,
      };

      // Send request
      axios
        .post("/api/v1/users/", form)
        // Handle success
        .then((res) => {
          this.$router.push("/log-in");
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
