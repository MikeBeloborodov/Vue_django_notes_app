<template>
  <div class="card">
    <div class="card-content">
      <p v-if="note.title" class="title is-size-4">{{ note.title }}</p>
      <p class="is-size-5">{{ note.body }}</p>
      <p class="is-size-5 is-italic mt-3">{{ note.created.slice(12, 16) }}</p>
      <p class="is-size-5 is-italic">{{ note.created.slice(0, 10) }}</p>
      <progress
        v-if="isLoading"
        class="progress is-small is-primary mt-4"
        max="100"
      ></progress>
    </div>
    <div class="card-footer">
      <a class="card-footer-item" @click="$emit('updateNote', note)">Update</a>
      <a class="card-footer-item" @click="deleteNote">Delete</a>
    </div>
  </div>
</template>

<script>
function sleep(time) {
  return new Promise((r) => setTimeout(r, time));
}
export default {
  props: ["note"],
  data() {
    return {
      isLoading: false,
    };
  },
  methods: {
    // async and sleep just for design purposes
    async deleteNote() {
      this.isLoading = true;
      await sleep(800);
      this.$emit("deleteNote", this.note.id);
    },
  },
};
</script>

<style scoped></style>
