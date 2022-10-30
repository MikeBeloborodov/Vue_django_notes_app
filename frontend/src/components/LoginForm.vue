<template>
  <div class="container">
    <form action="" @submit.prevent="">
      <div class="field">
        <label class="label">Email</label>
        <my-input v-model="loginForm.email" />
      </div>
      <div class="field">
        <label class="label">Password</label>
        <my-input type="password" v-model="loginForm.password" />
      </div>
      <div class="field">
        <div class="buttons is-right">
          <my-button @click="$emit('loginUser', loginForm)" class="is-primary"
            >Log-in</my-button
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
      loginForm: {
        email: "",
        password: "",
      },
    };
  },
  methods: {},
};
</script>

<style scoped></style>
