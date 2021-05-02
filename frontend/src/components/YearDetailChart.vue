<script>
    import {Line, mixins} from 'vue-chartjs'

    export default {
        extends: Line,
        mixins: [mixins.reactiveProp],
        props: ['showDetail', 'chartData'],
        data: () => ({
            options: {
                responsive: true,
                maintainAspectRatio: false,
                legend: {
                    labels: {
                        fontColor: "#d0d0d0",
                        fontSize: 14
                    }
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            fontColor: "#d0d0d0",
                            fontSize: 14,
                        }
                    }],
                    xAxes: [{
                        ticks: {
                            fontColor: "#d0d0d0",
                            fontSize: 14,
                        }
                    }]
                }
            },
        }),
        computed: {
            _chartData: function () {
                const _labels = this.chartData.map(period => {
                    return period.name
                })
                const maxAvg = this.chartData.map(period => {
                    return period.absMaxTemp
                })
                const minAvg = this.chartData.map(period => {
                    return period.avgMinTemp
                })
                return {
                    labels: _labels,
                    datasets: [
                        {
                            label: 'Max Temp',
                            backgroundColor: '#f87979',
                            data: maxAvg
                        },
                        {
                            label: 'Min Temp',
                            data: minAvg
                        }
                    ]
                }
            }
        },
        mounted() {
            this.renderChart(this._chartData, this.options)
        }
    }
</script>

<style>
  .chartjs-render-monitor {
    min-height: 400px;
  }
</style>
