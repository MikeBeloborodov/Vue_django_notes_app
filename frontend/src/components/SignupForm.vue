<template>
  <div class="container">
    <form action="" @submit.prevent="">
      <div class="field">
        <label class="label">Username</label>
        <my-input v-model="signupForm.username" />
      </div>
      <div class="field">
        <label class="label">Email</label>
        <my-input v-model="signupForm.email" />
      </div>
      <div class="field">
        <label class="label">Password</label>
        <my-input type="password" v-model="signupForm.password1" />
      </div>
      <div class="field">
        <label class="label">Confirm password</label>
        <my-input type="password" v-model="signupForm.password2" />
      </div>
      <div class="field">
        <div class="buttons is-right">
          <my-button @click="$emit('signupUser', signupForm)" class="is-primary"
            >Sign-up</my-button
          >
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      signupForm: {
        username: "",
        email: "",
        password1: "",
        password2: "",
      },
    };
  },
  methods: {},
};
</script>

<style scoped></style>
