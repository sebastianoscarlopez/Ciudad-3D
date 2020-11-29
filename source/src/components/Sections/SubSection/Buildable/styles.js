import { makeStyles } from '@material-ui/core/styles'

export default makeStyles((theme) => ({
  grid: {
    backgroundColor: '#F5F5F5',
    margin: theme.spacing(0.5),
    padding: theme.spacing(1)
  },
  gridItem: {
    marginBottom: theme.spacing(2)
  },
  button: {
    padding: 0
  },
  listado: {
    paddingLeft: 0
  },
  input: {
    width: 100,
    marginTop: -10
  }
}))
