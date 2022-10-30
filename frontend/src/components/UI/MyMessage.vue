<template>
		<div class="message is-danger">
				<div class="message-header">
						<p>Error</p>
						<div @click="$emit('closeMessage')" class="delete"></div>
				</div>
				<div class="message-content">
						<div class="content">
								<ul>
										<li 
										:key="message"
										class="pb-4"
										v-for="message in messages">
										{{ message }}
										</li>
								</ul>
						</div>
				</div>
		</div>
</template>

<script>
export default {
		name: 'my-message',
		props: ['messages']
}
</script>

<style scoped>

</style>
