// eslint-disable-next-line no-var
var configs = {
  urlConfigBase: 'configBase.json',
  includes: {
    urlAPI: 'https://epok.buenosaires.gob.ar',
    urlPhoto: 'https://fotos.usig.buenosaires.gob.ar',
    urlWsUsig: 'https://ws.usig.buenosaires.gob.ar',
    urlPDF: 'http://ssplan.buenosaires.gov.ar/man_atipicas/imagenes'
  },
  replaces: [
    {
      key: '{{urlVectorTile}}',
      value: 'https://vectortiles.usig.buenosaires.gob.ar/cur3d/'
    },
    {
      key: '{{urlBsAs}}',
      value: 'https://www.buenosaires.gob.ar/'
    },
    {
      key: '{{urlCDN2}}',
      value: 'https://cdn2.buenosaires.gob.ar/'
    },
    {
      key: '{{urlBoletin}}',
      value: 'https://documentosboletinoficial.buenosaires.gob.ar/publico/'
    },
    {
      key: '{{urlBsAsData}}',
      value: 'https://data.buenosaires.gob.ar/'
    },
    {
      key: '{{urlBcra}}',
      value: 'http://www.bcra.gov.ar/'
    },
    {
      key: '{{urlTAD}}',
      value: 'https://lbapw.agip.gob.ar/claveciudad'
    },
    {
      key: '{{urlUsig}}',
      value: 'https://servicios.usig.buenosaires.gob.ar'
    },
    {
      key: '{{urlCedom}}',
      value: 'http://www2.cedom.gob.ar/'
    },
    {
      key: '{{urlEpsg}}',
      value: 'https://epsg.org/'
    }
  ]
}
