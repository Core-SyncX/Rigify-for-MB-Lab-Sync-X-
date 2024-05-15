import bpy

class RIGIFYFORMBLAB_OT_var:
    fing_ik = 'index00_L', 'thumb01_L', 'thumb02_L', 'thumb03_L', 'index01_L', 'index02_L', 'index03_L', 'middle00_L', 'middle01_L', 'middle02_L', 'middle03_L', 'ring00_L', 'ring01_L', 'ring02_L', 'ring03_L', 'pinky00_L', 'pinky01_L', 'pinky02_L', 'pinky03_L', 'index00_R', 'thumb01_R', 'thumb02_R', 'thumb03_R', 'index01_R', 'index02_R', 'index03_R', 'middle00_R', 'middle01_R', 'middle02_R', 'middle03_R', 'ring00_R', 'ring01_R', 'ring02_R', 'ring03_R', 'pinky00_R', 'pinky01_R', 'pinky02_R', 'pinky03_R'

    fing_tweak = 'tweak_index03_L', 'tweak_index03_L.001', 'tweak_index02_L', 'tweak_index01_L', 'tweak_thumb03_L', 'tweak_thumb03_L.001', 'tweak_thumb02_L', 'tweak_thumb01_L', 'tweak_middle03_L', 'tweak_middle03_L.001', 'tweak_middle02_L', 'tweak_middle01_L', 'tweak_ring03_L', 'tweak_ring03_L.001', 'tweak_ring02_L', 'tweak_ring01_L', 'tweak_pinky03_L', 'tweak_pinky03_L.001', 'tweak_pinky02_L', 'tweak_pinky01_L', 'tweak_index03_R', 'tweak_index03_R.001', 'tweak_index02_R', 'tweak_index01_R', 'tweak_thumb03_R', 'tweak_thumb03_R.001', 'tweak_thumb02_R', 'tweak_thumb01_R', 'tweak_middle03_R', 'tweak_middle03_R.001', 'tweak_middle02_R', 'tweak_middle01_R', 'tweak_ring03_R', 'tweak_ring03_R.001', 'tweak_ring02_R', 'tweak_ring01_R', 'tweak_pinky03_R', 'tweak_pinky03_R.001', 'tweak_pinky02_R', 'tweak_pinky01_R'

    torso = 'pelvis', 'spine01', 'spine02', 'spine03', 'clavicle_L', 'clavicle_R', 'neck', 'head', 'breast_L', 'breast_R'

    arm_l_ik = 'upperarm_L', 'lowerarm_L', 'hand_L', 'lowerarm_twist_L', 'upperarm_twist_L'

    arm_l_fk = 'upperarm_fk_L', 'lowerarm_fk_L', 'hand_fk_L'

    arm_l_tweak = 'hand_tweak_L', 'lowerarm_tweak_L', 'lowerarm_tweak_L.001', 'upperarm_tweak_L.001', 'upperarm_tweak_L'

    arm_r_ik = 'upperarm_R', 'lowerarm_R', 'hand_R', 'lowerarm_twist_R', 'upperarm_twist_R'

    arm_r_fk = 'upperarm_fk_R', 'lowerarm_fk_R', 'hand_fk_R'

    arm_r_tweak = 'hand_tweak_R', 'lowerarm_tweak_R', 'lowerarm_tweak_R.001', 'upperarm_tweak_R.001', 'upperarm_tweak_R'

    leg_l_ik = 'thigh_L', 'calf_L', 'foot_L', 'toes_L', 'heel_L', 'calf_twist_L', 'thigh_twist_L'

    leg_l_fk = 'toes_L', 'thigh_fk_L', 'calf_fk_L', 'foot_fk_L'

    leg_l_tweak = 'foot_tweak_L', 'calf_tweak_L', 'calf_tweak_L.001', 'thigh_tweak_L.001', 'thigh_tweak_L'

    leg_r_ik = 'thigh_R', 'calf_R', 'foot_R', 'toes_R', 'heel_R', 'calf_twist_R', 'thigh_twist_R'

    leg_r_fk = 'toes_R', 'thigh_fk_R', 'calf_fk_R', 'foot_fk_R'

    leg_r_tweak = 'foot_tweak_R', 'calf_tweak_R', 'calf_tweak_R.001', 'thigh_tweak_R.001', 'thigh_tweak_R'

    ik = fing_ik, torso, arm_l_ik, arm_r_ik, leg_l_ik, leg_r_ik

    arm = arm_l_fk, arm_r_fk, arm_l_tweak, arm_r_tweak

    leg = leg_l_fk, leg_r_fk, leg_l_tweak, leg_r_tweak


    #VARIABLES NEEDED FOR FK AND TWEAKS; WILL BE IMPLEMENTED IN GENERATE_RIG.PY
  
    db = [{'bname': ['thumb','index','middle','ring','pinky'],
                'ik_L': 0, 'ik_R': 0, 'tweak_L': 1, 'tweak_R': 1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['hand'],
                'ik_L': 4, 'ik_R': 7, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['lowerarm'],
                'ik_L': 4, 'ik_R': 7, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['upperarm'],
                'ik_L': 4, 'ik_R': 7, 'tweak_L': 6, 'tweak_R': 9,
                'fk_L': 5, 'fk_R': 8},
                {'bname': ['clavicle'],
                'ik_L': 2, 'ik_R': 2, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['breast'],
                'ik_L': 2, 'ik_R': 2, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['pelvis'],
                'ik_L': 2, 'ik_R': 2, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['thigh'],
                'ik_L': 10, 'ik_R': 13, 'tweak_L': 12, 'tweak_R': 15,
                'fk_L': 11, 'fk_R': 14},
                {'bname': ['calf'],
                'ik_L': 10, 'ik_R': 13, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['foot'],
                'ik_L': 10, 'ik_R': 13, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['toes'],
                'ik_L': 10, 'ik_R': 13, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['head'],
                'ik_L': 2, 'ik_R': 2, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['neck'],
                'ik_L': 2, 'ik_R': 2, 'tweak_L': -1, 'tweak_R': -1,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['spine03'],
                'ik_L': 2, 'ik_R': 2, 'tweak_L': 3, 'tweak_R': 3,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['spine02'],
                'ik_L': 2, 'ik_R': 2, 'tweak_L': 3, 'tweak_R': 3,
                'fk_L': -1, 'fk_R': -1},
                {'bname': ['spine01'],
                'ik_L': 2, 'ik_R': 2, 'tweak_L': 3, 'tweak_R': 3,
                'fk_L': -1, 'fk_R': -1}]