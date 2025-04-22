<template>
  <div class="image-upload">
    <div class="upload-container" @click="triggerFileInput" @dragover.prevent @drop.prevent="handleDrop">
      <input
        type="file"
        ref="fileInput"
        @change="handleFileChange"
        accept="image/*"
        style="display: none"
      />
      <div v-if="!selectedFile" class="upload-placeholder">
        <i class="fas fa-cloud-upload-alt"></i>
        <p>Перетащите изображение сюда или нажмите для выбора</p>
      </div>
      <div v-else class="preview-container">
        <img :src="previewUrl" alt="Preview" class="preview-image" />
        <div class="preview-overlay">
          <button @click.stop="removeFile" class="remove-btn">
            <i class="fas fa-times"></i>
          </button>
        </div>
      </div>
    </div>
    <div class="description-input" v-if="selectedFile">
      <textarea
        v-model="description"
        placeholder="Введите описание изображения"
        rows="3"
      ></textarea>
    </div>
    <button
      class="upload-btn"
      @click="uploadImage"
      :disabled="!selectedFile || uploading"
    >
      {{ uploading ? 'Загрузка...' : 'Загрузить' }}
    </button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ImageUpload',
  data() {
    return {
      selectedFile: null,
      previewUrl: '',
      description: '',
      uploading: false
    };
  },
  methods: {
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    handleFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.selectedFile = file;
        this.previewUrl = URL.createObjectURL(file);
      }
    },
    handleDrop(event) {
      const file = event.dataTransfer.files[0];
      if (file && file.type.startsWith('image/')) {
        this.selectedFile = file;
        this.previewUrl = URL.createObjectURL(file);
      }
    },
    removeFile() {
      this.selectedFile = null;
      this.previewUrl = '';
      this.description = '';
    },
    async uploadImage() {
      if (!this.selectedFile) return;

      this.uploading = true;
      const formData = new FormData();
      formData.append('image', this.selectedFile);
      formData.append('description', this.description);

      try {
        const response = await axios.post('/api/images/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.$emit('upload-success', response.data);
        this.removeFile();
      } catch (error) {
        console.error('Error uploading image:', error);
        this.$emit('upload-error', error);
      } finally {
        this.uploading = false;
      }
    }
  }
};
</script>

<style scoped>
.image-upload {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.upload-container {
  border: 2px dashed #ccc;
  border-radius: 8px;
  padding: 20px;
  text-align: center;
  cursor: pointer;
  transition: border-color 0.3s;
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.upload-container:hover {
  border-color: #666;
}

.upload-placeholder {
  color: #666;
}

.upload-placeholder i {
  font-size: 48px;
  margin-bottom: 10px;
}

.preview-container {
  position: relative;
  width: 100%;
  max-width: 400px;
}

.preview-image {
  max-width: 100%;
  max-height: 300px;
  border-radius: 8px;
}

.preview-overlay {
  position: absolute;
  top: 10px;
  right: 10px;
}

.remove-btn {
  background: rgba(255, 255, 255, 0.8);
  border: none;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.remove-btn:hover {
  background: rgba(255, 255, 255, 1);
}

.description-input {
  margin-top: 20px;
}

.description-input textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
}

.upload-btn {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  width: 100%;
}

.upload-btn:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.upload-btn:hover:not(:disabled) {
  background-color: #45a049;
}
</style> 