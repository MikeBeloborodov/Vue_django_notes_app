<template>
		<div class="modal">
				<div class="modal-background" @click="$emit('closeModal')"></div>
				<div class="modal-content">
						<div class="card">
								<slot></slot>
						</div>
				</div>
				<button @click="$emit('closeModal')" class="modal-close is-large"></button>
		</div>
</template>

<script>
export default {
		name: 'my-modal'	
}
</script>

<style scoped>

</style>
