<template>
  <textarea
    class="textarea"
    :value="modelValue"
    @input="update"
    placeholder="Text area"
  >
				<slot></slot>
		</textarea>
</template>

<script>
export default {
  name: "my-textarea",
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
