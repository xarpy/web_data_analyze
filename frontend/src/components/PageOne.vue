<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
    <h1 class="display-4">Dataset</h1>
    <hr class="my-4">
    <div class="card text-center">
  <div class="card-header">
    File
  </div>
  <div class="card-body">
    <h5 class="card-title">Inserted dataset file in format .csv</h5>
    <p class="card-text">
    <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
    </p>
    <button type="button" class="btn btn-primary" v-on:click="submitFile()">Submit</button>
  </div>
</div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'PageOne',
  data() {
    return {
      file: '',
    };
  },
  methods: {
    submitFile() {
      const formData = new FormData();
      formData.append('file', this.file);
      axios.post('http://localhost:5000/data/inserted', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }).then((res) => {
        this.msg = res.data;
      }).catch((error) => {
        console.log(error);
      });
    },
    handleFileUpload() {
      const value = this.$refs.file.files[0];
      this.file = value;
    },
  },
};
</script>
