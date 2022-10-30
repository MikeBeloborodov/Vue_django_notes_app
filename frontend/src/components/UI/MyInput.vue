<template>
  <input
    type="text"
    :value="modelValue"
    class="input"
    @input="update"
    placeholder="Text input"
  />
</template>

<script>
export default {
  name: "my-input",
  props: {
    modelValue: [String, Number],
  },
  methods: {
    update(event) {
      this.$emit("update:modelValue", event.target.value);
    },
  },
};
</script>

<style scoped></style>
