<template>
		<div class="container">
				<div class="title">New note</div>
				<form action="" @submit.prevent>
						<div class="field">
								<label class="label">Title</label>
								<my-input v-model="noteForm.title" />
						</div>
						<div class="field">
								<label class="label">Text</label>
								<my-textarea v-model="noteForm.body"/>
						</div>
						<div class="field">
								<div class="buttons is-right">
										<my-button
										@click="$emit('postNote', noteForm)"
										class="is-primary">Post</my-button>
								</div>
						</div>
				</form>
		</div>
</template>

<script>
export default {
		data(){
				return {
						noteForm: {
								title: "",
								body: ""
						}
				}
		}
}
</script>

<style scoped>

</style>
