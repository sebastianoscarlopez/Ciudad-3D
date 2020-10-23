import React, { useEffect } from 'react'

import PropTypes from 'prop-types'

import {
  Box, Typography, IconButton,
  TableContainer, Table, TableHead, TableRow,
  TableCell, TableBody, makeStyles
} from '@material-ui/core'
import ArrowBackIcon from '@material-ui/icons/ArrowBack'
import ContainerBarWorks from 'components/Sections/ContainerBarWorks'

import useFontsStyles from 'theme/fontsDecorators'

import { actions as categoriesActions } from 'state/ducks/categories'
import { actions as worksActions } from 'state/ducks/works'

import { useDispatch, useSelector } from 'react-redux'

import { getWorksGroups, getColumnsWorksByWorksId } from 'utils/configQueries'

import useStyles from './styles'

function createData(expte, fecha, tipoObra, superficie, destino) {
  return {
    expte, fecha, tipoObra, superficie, destino
  }
}

const rows = [
  createData('---', 159, 6.0, 24, 4.0),
  createData('---', 237, 9.0, 37, 4.3),
  createData('---', 262, 16.0, 24, 6.0),
  createData('---', 305, 3.7, 67, 4.3),
  createData('---', 356, 16.0, 49, 3.9)
]

const Data = ({ styles: { tableCell } }) => (
  <TableBody>
    {rows.map((row) => (
      <TableRow key={row.name}>
        <TableCell className={tableCell}>{row.expte}</TableCell>
        <TableCell className={tableCell}>{row.fecha}</TableCell>
        <TableCell className={tableCell}>{row.tipoObra}</TableCell>
        <TableCell className={tableCell}>{row.superficie}</TableCell>
        <TableCell className={tableCell}>{row.destino}</TableCell>
      </TableRow>
    ))}
  </TableBody>
)

const Columns = ({ id, styles: { bold, tableCell } }) => (
  <TableContainer>
    <Table>
      <TableHead>
        <TableRow>
          {
            getColumnsWorksByWorksId(id).map((column, idx) => (
              // eslint-disable-next-line react/no-array-index-key
              <TableCell key={idx} className={tableCell}>
                <Typography variant="subtitle2" className={bold}>
                  {column}
                </Typography>
              </TableCell>
            ))
          }
        </TableRow>
      </TableHead>
      <Data styles={{ tableCell }} />
    </Table>
  </TableContainer>
)

const Works = () => {
  const classes = useStyles()
  const decorators = useFontsStyles()
  // const data = useSelector((state) => state.works.data)
  const dispatch = useDispatch()
  const smp = useSelector((state) => state.basicData.data.smp)

  useEffect(() => {
    dispatch(worksActions.clickOnParcel(smp))
  }, [dispatch, smp])

  return (
    <ContainerBarWorks>
      <Typography
        variant="h5"
        className={`${decorators.bold} ${decorators.marginTop_md} ${decorators.marginBottom_xl}`}
      >
        Información
      </Typography>
      <Box className={classes.subTitle}>
        <Typography variant="h6" className={decorators.bold}>
          <IconButton
            onClick={() => dispatch(categoriesActions.sectionBack())}
            className={classes.button}
          >
            <ArrowBackIcon />
          </IconButton>
          Obras
        </Typography>
      </Box>
      <Box className={classes.boxContainer}>
        {
            getWorksGroups().map(({ id, title }) => (
              <Box className={classes.boxSubContainer} key={id}>
                <Typography variant="subtitle1" className={`${decorators.bold} ${decorators.marginTop_md} ${decorators.marginBottom_ml}`}>
                  {title}
                </Typography>
                <Columns id={id} styles={{ ...decorators, ...classes }} />
              </Box>
            ))
          }
      </Box>
    </ContainerBarWorks>
  )
}

Columns.propTypes = {
  id: PropTypes.string.isRequired,
  bold: PropTypes.string.isRequired,
  tableCell: PropTypes.string.isRequired,
  styles: PropTypes.objectOf(makeStyles).isRequired
}

Data.propTypes = {
  tableCell: PropTypes.string.isRequired,
  styles: PropTypes.objectOf(makeStyles).isRequired
}

export default Works
