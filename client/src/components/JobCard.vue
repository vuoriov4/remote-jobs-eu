<template>
  <div class="job" :ref="job.id">
    <div class="job-rating" @click="$emit('select-company', job)">
      Rated {{ job.gd_overall_rating || '5.0' }}/5.0
      <img width="20px" src="glassdoor.png"/>
    </div>
    <div class="job-title">{{ job.title }}</div>
    <hr/>
    <div class="job-date" v-if="job.date">{{ timeSince(new Date(Date.parse(job.date))) }} ago</div>
    <div class="job-company">{{ job.company }}</div>
    <div class="job-summary">
      {{ job.description.slice(0, 200) }}... 
    </div>
    <div class="job-actions"><a  @click="$emit('select-job-description', job)">Read more</a></div>
    <div class="job-location" @click="$emit('select-location', job)" v-if="job.place && job.location">
      {{ job.place }} (Remote) 🌍 
    </div>
  </div>
</template>

<script>
  export default {
    name: 'JobCard',
    components: {},
    props: ['job'],
    data() {
      return {};
    },
    watch: {
    },
    methods: {
      timeSince(date) {
        const seconds = Math.floor((new Date() - date) / 1000);
        let interval = seconds / 31536000;
        if (interval > 1) {
          return Math.floor(interval) + " years";
        }
        interval = seconds / 2592000;
        if (interval > 1) {
          return Math.floor(interval) + " months";
        }
        interval = seconds / 86400;
        if (interval > 1) {
          return Math.floor(interval) + " days";
        }
        interval = seconds / 3600;
        if (interval > 1) {
          return Math.floor(interval) + " hours";
        }
        interval = seconds / 60;
        if (interval > 1) {
          return Math.floor(interval) + " minutes";
        }
        return Math.floor(seconds) + " seconds";
      }
    },
    mounted() {
    }
  };
</script>

<style >
.job {
    width: calc(100% - 100px);
    background: rgba(80,80,80,1.0);
    margin: 15px 30px 25px 30px;
    background: white;
    box-shadow: 0px 0px 5px rgba(0,0,0,0.25);
    padding: 20px 20px 20px 20px;
    height: auto;
    font-size: 16px;
  }
  .job-title {
    font-weight: bold;
    text-overflow: ellipsis;
    font-size: 20px;
    padding-bottom: 20px;
  }
  .job-company {
    color: #a0a0a0;
    font-size: 14px;
    margin-bottom: -15px;
  }
  .job-summary {
    margin-top: 20px;
    font-size: 16px;
  }
  .job-location {
    float: right;
    font-size: 14px;
    margin: -20px 0px 5px 0px;
    cursor: pointer;
  }
  .job-date {
    float: right;
    color: #a0a0a0;
    font-size: 14px;
    margin-bottom: -15px;
  }
  .job-salary {
    float: right;
    padding: 5px;
    margin: 3px;
    font-size: 14px;
    line-height: 14px;
  }
  .job-rating {
    float: right;
    margin: 2px -6px 0px 20px;
    font-size: 15px;
    cursor: pointer;
  }
  .job-rating > img {
    margin-left: 10px;
  }
  .job-linkedin {
    font-size: 14px;
    line-height: 14px;
    padding: 5px;
    float: right;
    transform: translate(0px, 0px);
    cursor: pointer;
  }
  .job-rating > img, .job-linkedin > img {
    transform: translate(-7px, 5px);
  }
  .job-actions {
    margin-top: 10px;
    cursor: pointer;
  }
  .job-actions > button {
    background: white;
    padding: 3px 5px 3px 5px;
    margin-right: 5px;
    border: 1px solid #808080;
    cursor: pointer;
  }
</style>