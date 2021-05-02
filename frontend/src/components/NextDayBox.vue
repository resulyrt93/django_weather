<template>
  <div class="col-sm-12 next-day-box">
    <div class="col-sm-8 forecast-main">
      <div class="row d-flex flex-column">
        <p>{{weekday}}</p>
        <h5>{{dayConditions.avgtempC}}°</h5>
      </div>
    </div>
    <div class="col-sm-4 forecast-min-low">
      <p>
        <span>{{dayConditions.maxtempC}}°</span>
      </p>
      <p>
        <span>{{dayConditions.mintempC}}°</span>
      </p>
    </div>
  </div>
</template>

<script>
    import moment from 'moment'

    export default {
        name: "NextDayBox",
        props: ['dayConditions'],
        computed: {
            weekday: function () {
                return moment(this.dayConditions.date).format('dddd');
            }
        }
    }
</script>

<style scoped>

  .next-day-box {
    display: inline-flex;
    margin: 14px auto;
    padding: 0px 5px;
  }
</style>
