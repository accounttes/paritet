<template>
  <div class="upload-page">
    <h2>Загрузка изображения</h2>
    <ImageUploadComponent
      @upload-success="handleUploadSuccess"
      @upload-error="handleUploadError"
    />
  </div>
</template>

<script>
import ImageUploadComponent from '@/components/ImageUpload.vue'

export default {
  name: 'ImageUploadView',
  components: {
    ImageUploadComponent
  },
  methods: {
    handleUploadSuccess(response) {
      this.$router.push('/');
    },
    handleUploadError(error) {
      alert('Ошибка при загрузке изображения. Пожалуйста, попробуйте снова.');
    }
  }
}
</script>

<style scoped>
.upload-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h2 {
  margin-bottom: 30px;
  text-align: center;
}
</style> 