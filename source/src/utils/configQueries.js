// import config from 'appConfig.json'
import icons from 'utils/svgIcons'

let config = null
const init = async () => {
  if (config !== null) {
    return
  }
  const url = process.env.REACT_APP_URL_CONFIG || 'https://epok.buenosaires.gob.ar/cur3d/config/?environment=dev'
  config = await fetch(url)
    .then((data) => data.json())
}
// Métodos que devuelven mucha data y puede no ser serializable
const getFullLayerConfig = (idGroup, idLayer) => config
  .layersGroup.find((g) => g.id === idGroup)
  .layers.find((l) => l.id === idLayer)

// Métodos que retornan data acotada y segura de serializar
const getCategories = () => config.categories.map(
  ({ id, title, path }) => ({ id, title, path: icons.find((i) => i.id === path).path })
)

const getLayersGroups = () => config.layersGroup.map(({ id, title }) => ({
  id,
  title
}))

const getLayersByLayersGroupId = (layersGroupId) => config
  .layersGroup.find((l) => l.id === layersGroupId)
  .layers.map(({
    id, title, color, index
  }) => ({
    id,
    title,
    color,
    index
  }))

const getWorksGroups = () => config.works.map(({ id, title, columns }) => ({
  id,
  title,
  columns
}))

const getInspectionsGroups = () => config.inspections.map(({ id, title, columns }) => ({
  id,
  title,
  columns
}))

const getInformation = () => config.information.map(({
  id, title, description, color
}) => ({
  id, title, description, color
}))

const getBasicData = () => config.basicData.map(({
  title, fill, format, isNumber
}) => ({
  title, fill, format, isNumber
}))

const getCapitalGain = () => config.capitalGain.map(({ title, fill, format }) => ({
  title, fill, format
}))

const getBuildable = () => config.buildable.map(({
  title, items, isArea, isPlusvalia, large
}) => ({
  title, items, isArea, isPlusvalia, large
}))

const getUsesTable = async () => config.uses.map(({
  id, title, desc, afluencia, icons: icon
}) => ({
  id,
  title,
  desc,
  afluencia,
  iconsData: icon.map(({ title: iconTitle, svgId }) => (
    { iconTitle, svgId }
  ))
}))

const getAffectationsTable = async () => config.affectations.map(({
  id, title, subtitle, desc
}) => ({
  id,
  title,
  subtitle,
  desc
}))

const getExplorerFilters = () => config.explorerFilters.map(({
  id, filterId, title
}) => ({
  id, filterId, title
}))

const getFullExplorerLayerConfig = (idExplorer) => config
  .explorerFilters.find((g) => g.id === idExplorer).layers

const getExplorerOptions = (idExplorer) => config.explorer.filter((c) => c.id === idExplorer)

const getExplorer = () => config.explorer

const getAlert = (idAlert) => config.alerts.find(({ id }) => id === idAlert).text

const getCategoryTitle = (idCategory) => config.categories.find(({ id }) => id === idCategory).title

const getSectionTitle = (idTitle) => config.information.find(({ id }) => id === idTitle).title

const getApiUrl = () => config.urlAPI

export {
  init, getCategories, getFullLayerConfig, getInformation, getBasicData,
  getLayersGroups, getLayersByLayersGroupId, getBuildable, getExplorer,
  getUsesTable, getWorksGroups, getAffectationsTable, getExplorerOptions,
  getExplorerFilters, getCapitalGain, getInspectionsGroups, getAlert,
  getCategoryTitle, getSectionTitle, getFullExplorerLayerConfig, getApiUrl
}
