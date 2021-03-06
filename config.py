def getConfig():
    settings = {}
    settings['source'] = './sources/sapo-160.wav'
    settings['overlap'] = 2
    settings['coded-file'] = 'bn-coded-file'
    settings['lstm-file'] = 'bn-lstm-file'
    settings['phase-encoder'] = 'bn-phase-encoder'
    settings['magnitude-encoder'] = 'bn-magnitude-encoder'
    settings['phase-result'] = 'bn-phase-result'
    settings['magnitude-result'] = 'bn-magnitude-result'
    settings['lstm-epoch'] = 200
    settings['ae-epoch'] = 200
    settings['section-count'] = 8
    settings['ae-iteration'] = 40
    settings['lstm-iteration'] = 30
    settings['block-count'] = 175
    settings['layer-count'] = 4
    settings['sample-rate'] = 16000
    settings['dim-decrease'] = 250
    settings['load-weights'] = True
    settings['dropout'] = 0.4
    return settings
