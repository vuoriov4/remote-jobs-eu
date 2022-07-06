<template>
  <div>
    <div><h2 id="search-results-title">
      Search results
    </h2></div>
    <div id="sort" class="search-select">Sort by
      <select @change="onOrderByChange">
        <option selected value="relevance">Relevance</option>
        <option value="timestamp">Most recent</option>
        <option value="gd_overall_rating">GD rating: Overall</option>
        <option value="gd_benefits_rating">GD rating: Compensation</option>
        <option value="gd_revenue">Company revenue</option>
      </select>
    </div>
    <div id="num-results" class="search-select">Show
      <select @change="onNumResultsChange">
        <option value="10">10 results</option>
        <option selected value="50">50 results</option>
        <option value="100">100 results</option>
      </select>
    </div>
    <div id="created-since" class="search-select">Since
      <select @change="onCreatedSinceChange">
        <option :value="parseInt((Date.now() / 1000) - 60 * 60 * 24)">24 hours</option>
        <option selected :value="parseInt((Date.now() / 1000) - 60 * 60 * 24 * 7)">7 days</option>
        <option :value="parseInt((Date.now() / 1000) - 60 * 60 * 24 * 30)">1 month</option>
        <option :value="parseInt((Date.now() / 1000) - 60 * 60 * 24 * 365)">1 year</option>
      </select>
    </div>
    <div class="jobs">
      <p v-if="jobs.length == 0">Try again with another search term.</p>
      <job-card 
        @select-job-description="data => $emit('select-job-description', data)"
        @select-company="data => $emit('select-company', data)" 
        @select-location="data => $emit('select-location', data)"
        :job="job" v-for="(job, i) in jobs" v-bind:key="'job-' + i">
      </job-card>
    </div>
  </div>
</template>

<script>
  import JobCard from './JobCard.vue';
  
  export default {
    name: 'JobList',
    components: { JobCard },
    props: [ 'response' ],
    data() {
      return {
        jobs: [],
      };
    },
    watch: {
      response: {
        immediate: true, 
        handler(r) {
          this.jobs = r.jobs;
        }
      },
    },
    methods: {
      onOrderByChange(e) {
        this.$emit('select-order-by', e);
      },
      onNumResultsChange(e) {
        this.$emit('select-num-results', e);
      },
      onCreatedSinceChange(e) {
        this.$emit('select-created-since', e);
      },
      /*sortBy(field) {
        const criteria = {
          'date': (x) => { return Date.parse(x) || 0; },
          'gd_overall_rating': (x) => { return parseFloat(x) || 0; },
          'gd_benefits_rating': (x) => { return parseFloat(x) || 0; },
          'gd_revenue': (x) => { 
            let r = parseInt(x.split(' ')[0].slice(1)) || 0;
            if (x.includes('million')) r *= 10e6;
            else if (x.includes('billion')) r *= 10e9;
            else if (x.includes('trillion')) r *= 10e12;
            return r; 
          },
        };
        const c = field;
        const s = [ ...this.jobs ];
        s.sort((a, b) => {
          return criteria[c](b[c]) - criteria[c](a[c]);
        });
        this.jobs = s;
      },*/
    },
    mounted() {
    },
  };
</script>

<style>
  p {
    margin: 30px;
  }
  #search-results-title {
    margin: 0px;
    padding: 25px 0px 10px 30px;
    display: inline-block;
  }
  .search-select {
    font-size: 16px;
    display: inline-block;
  }
  #sort {
    margin: 10px 10px 0px 30px;
  }
  #num-results {
    margin: 0px 0px 0px 0px;
  }
  #created-since {
    margin: 0px 0px 0px 10px;
  }
  .search-select > select {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 16px;
  }
  .job:first-of-type {
    margin-top: 30px;
  }
  
</style>