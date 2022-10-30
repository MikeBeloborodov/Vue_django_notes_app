<template>
	<my-modal 
		@closeModal="this.showModal = false"
		:class="{'is-active': showModal}">
		<UpdateForm @submitUpdate="submitUpdate" :note_to_update="note_to_update"/>
	</my-modal>
	<my-message @closeMessage="closeMessage" v-if="showMessages" :messages="messages"/>
	<div class="columns">
		<div class="column">
			<NoteForm @postNote="postNote" style="max-width: 35rem"/>	
			<progress v-if="isLoading" class="progress is-small is-primary mt-6" max="100"></progress>
		</div>
		<div class="column is-1"></div>
		<div class="column">
			<div v-if="notes.length == 0" class="title is-size-4">Notes are empty.</div>
			<div v-if="notes.length == 0" class="is-size-5">You can post something using the form.</div>
			<NoteCard 
			@updateNote="updateNote"
			@deleteNote="deleteNote"
			v-for="note in notes" 
			:key="note.id" 
			:note="note" 
			style="max-width:40rem"
			class="mb-5"/>		
		</div>
	</div>
</template>

<script>
import NoteForm from '@/components/NoteForm.vue';
import NoteCard from '@/components/NoteCard.vue';
import UpdateForm from '@/components/UpdateForm.vue';
import axios from 'axios'

function sleep(time){
		return new Promise(r => setTimeout(r, time))
}

export default {
		data(){
				return {
						notes: [],
						messages: [],
						showMessages: false,
						isLoading: false,
						note_to_update: {
						},
						showModal: false
				}
		},
		components: {
				NoteForm, NoteCard, UpdateForm
		},
		beforeMount(){
				axios
						.get('api/v1/notes/')
						.then(res => {
								this.notes = res.data.notes
						})
						.catch(error => {
								console.log(error)
								this.messages.push(error.message)	
								this.showMessages = true
						})
		},
		methods: {
			async	postNote(note_form){
						this.closeMessage()
						this.isLoading = true
						await sleep(800)
						axios
								.post('api/v1/notes/', note_form)
								.then(res => {
										axios
												.get('api/v1/notes/')
												.then(res => {
														this.notes = res.data.notes
												})
												.catch(error => {
														this.messages.push(error.message)	
														this.showMessages = true
												})
												this.isLoading = false
								})
								.catch(error => {
										this.messages.push(error.message)	
										this.showMessages = true
								})
				},
				deleteNote(note_id){
						this.closeMessage()
						axios
								.delete('api/v1/notes/' + note_id)
								.then(res => {
										axios
												.get('api/v1/notes/')
												.then(res => {
														this.notes = res.data.notes
												})
												.catch(error => {
														this.messages.push(error.message)	
														this.showMessages = true
												})
								})
								.catch(error => {
										this.messages.push(error.message)	
										this.showMessages = true
								})
				},
				updateNote(note){
						this.note_to_update = Object.assign({}, note)
						this.showModal = true
				},
				submitUpdate(){
						const form = {
								title: this.note_to_update.title,
								body: this.note_to_update.body
						}
						axios
								.put('api/v1/notes/' + this.note_to_update.id, form)
								.then(res => {
										this.showModal = false
										axios
												.get('api/v1/notes/')
												.then(res => {
														this.notes = res.data.notes
												})
												.catch(error => {
														this.messages.push(error.message)	
														this.showMessages = true
												})
								})
								.catch(error => {
										this.messages.push(error.message)	
										this.showMessages = true
								})
				},
				closeMessage(){
						this.messages = []
						this.showMessages = false
				}
		},
}
</script>

<style>

</style>
