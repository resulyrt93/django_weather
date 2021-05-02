<template>
  <div class="col-xs-12 col-sm-12 col-md-3 row" style="text-align: right;">
    <div class="col-md-12 col-sm-3 col-xs-3 side-weather-info">
      <h6>Humidity:
        <span>{{currentCondition.humidity}}</span>
        %
      </h6>
    </div>
    <div class="col-md-12 col-sm-3 col-xs-3 side-weather-info">
      <h6>Wind:
        <span>{{currentCondition.windspeedKmph}}</span>
        KMPH
      </h6>
    </div>
    <div class="col-md-12 col-sm-3 col-xs-3 side-weather-info">
      <h6>High:
        <span>{{todayDetail.maxtempC}}</span>
        °
      </h6>
    </div>
    <div class="col-md-12 col-sm-3 col-xs-3 side-weather-info">
      <h6>Low:
        <span>{{todayDetail.mintempC}}</span>
        °
      </h6>
    </div>
  </div>
</template>

<script>
    export default {
        name: "CardRightDetails",
        props: ['currentCondition', 'todayDetail']
    }
</script>

<style scoped>
  .side-weather-info {
    padding: 0px 10px;
  }
</style>
