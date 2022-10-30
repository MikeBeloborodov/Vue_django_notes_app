<template>
		<div class="container p-5">
				<form action="" @submit.prevent>
						<div class="field">
								<label class="label">Title</label>
								<my-input v-model="note_to_update.title" />
						</div>
						<div class="field">
								<label class="label">Text</label>
								<my-textarea v-model="note_to_update.body" />
						</div>
						<div class="field">
								<div class="buttons is-right">
										<my-button
										@click="submitUpdate" 
										:class="{'is-loading': isLoading}"
										class="button is-primary">Update</my-button>
								</div>
						</div>
				</form>
		</div>
</template>

<script>

function sleep(time){
		return new Promise(r => setTimeout(r, time))
}

export default {
		data(){
				return {
						isLoading: false
				}
		},
		props: ['note_to_update'],
		methods: {
				async submitUpdate(){
						this.isLoading = true	
						await sleep(800)
						this.$emit('submitUpdate')
						this.isLoading = false
				}
		}
}
</script>

<style scoped>

</style>
