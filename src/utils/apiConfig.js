const getParcel = ({ lng, lat }) => `https://epok.buenosaires.gob.ar/catastro/parcela/?lng=${lng}&lat=${lat}`

const getParcelBySmp = (smp) => `https://epok.buenosaires.gob.ar/catastro/parcela/?smp=${smp}`

const getGeometrical = (smp) => `https://epok.buenosaires.gob.ar/catastro/geometria/?smp=${smp}`

const getBuildable = (smp) => `https://epok.buenosaires.gob.ar/cur3d/seccion_edificabilidad/?smp=${smp}`

const getCapitalGain = (smp) => `https://epok.buenosaires.gob.ar/cur3d/calcular_plusvalia/?smp=${smp}`

const getUses = (smp) => `https://epok.buenosaires.gob.ar/cur3d/mixtura_usos/?smp=${smp}`

const getAffectations = (smp) => `https://epok.buenosaires.gob.ar/catastro/afectaciones/?smp=${smp}`

export {
  getParcel, getParcelBySmp, getGeometrical, getBuildable, getCapitalGain, getUses, getAffectations
}
