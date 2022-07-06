<template>
  <div>
    <h2>{{ job.title }}</h2>
    <hr/>
    <div id="embed"></div>
    <br>
    <h3><a :href="job.link">View this job on LinkedIn</a></h3>
    <h3><a :href="job.apply_link" v-if="job.apply_link">Apply</a></h3>
    <button class="close-btn" @click="$emit('close', true)">❌</button>
  </div>
</template>

<script>
  export default {
    name: 'JobDescription',
    components: {},
    props: ['job'],
    data() {
      return {};
    },
    watch: {
      job() {
        this.embedHtml();
      }
    },
    methods: {
      embedHtml() {
        if (!this.job || !this.job.description_html) return;
        const elem = document.getElementById('embed');
        elem.innerHTML = this.job.description_html.trim();
      }
    },
    mounted() {
      this.embedHtml();
    }
  };
</script>

<style >
h2 {
  margin-top: 0px;
}
</style>