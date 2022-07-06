<template>
  <div>
    <h2>{{ job.company }}</h2>
    <hr/>
    <h3>Company info</h3>
    <div>Employees <div class="company-info-value">{{ job.gd_employees }}</div></div>
    <div>Industry <div class="company-info-value">{{ job.gd_industry }}</div></div>
    <div>Revenue <div class="company-info-value">{{ job.gd_revenue }}</div></div>
    <div>Website <div class="company-info-value">{{ job.gd_website }}</div></div>
    <h3>Employee rating</h3>
    <div class="rating">Overall <div class="rating-value">{{ job.gd_overall_rating }}/5.0</div> </div>
    <div class="rating">Compensation and benefits <div class="rating-value">{{ job.gd_benefits_rating }}/5.0</div>  </div>
    <div class="rating">Career opportunities <div class="rating-value">{{ job.gd_career_rating }}/5.0</div> </div>
    <div class="rating">Culture and values <div class="rating-value">{{ job.gd_culture_rating }}/5.0</div> </div>
    <div class="rating">Work-life balance <div class="rating-value">{{ job.gd_worklife_rating }}/5.0</div> </div>
    <div class="rating">Upper management  <div class="rating-value">{{ job.gd_management_rating }}/5.0</div> </div>
    <div class="rating">Diversion and inclusion <div class="rating-value">{{ job.gd_diversity_rating }}/5.0</div> </div>
    <button class="close-btn" @click="$emit('close', true)">❌</button>
    <br>
    <h3>
      <a target="_blank" 
        :href="job.gd_source || 'www.glassdoor.com'">
        View this company on Glassdoor
      </a>
    </h3>
  </div>
</template>

<script>
  export default {
    name: 'Ratings',
    components: {},
    props: ['job'],
    data() {
      return {};
    },
  };
</script>

<style>
.rating-value {
  float: right;
  font-weight: bold;
}
.company-info-value {
  float: right;
  font-weight: bold;
}
</style>