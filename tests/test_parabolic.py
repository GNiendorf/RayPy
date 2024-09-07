import tracepy as tp

mirror = {
    'action': 'reflection',
    'P': 1.5,
    'kappa': 0.,
    'c': -.5,
    'Diam': 2.2,
}

stop = {
    'action': 'stop',
    'P': .5,
    'Diam': .2
}

def test_rms_parabolic():
    geo = [mirror, stop]
    ray_group = tp.ray_plane(geo, [0., 0., -1.5], 1.1, d=[0.,0.,1.], nrays=100)
    rms = tp.spotdiagram(geo, ray_group, optimizer=True)
    assert rms == 0.
