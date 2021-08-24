"""
This type stub file was generated by pyright.
"""

def filter_data(data, labels, diffs=...): # -> tuple[dict[Unknown, Unknown], Unknown]:
    """Filters the data to fit the given labels and difficulties.
    Args:
        data (dict): Dictionary with the data (as numpy arrays).
            {
                'label':      [...], # expected
                'difficulty': [...]  # if diffs not None
                ...
            }
        labels (number[]): List of labels which should be maintained.
        difficulties (number[]): List of difficulties which should maintained.
            (optional)

    Returns:
        Tuple wit dictionary with same as format as input, with only the given labels
        and difficulties and the indices.
    """
    ...

def precision_3d(pred, target, classes=..., difficulties=..., min_overlap=..., bev=..., similar_classes=...): # -> tuple[ndarray[Unknown, Unknown], ndarray[Unknown, Unknown]]:
    """Computes precision quantities for each predicted box.
    Args:
        pred (dict): Dictionary with the prediction data (as numpy arrays).
            {
                'bbox':       [...],
                'label':      [...],
                'score':      [...],
                'difficulty': [...],
                ...
            }
        target (dict): Dictionary with the target data (as numpy arrays).
            {
                'bbox':       [...],
                'label':      [...],
                'difficulty': [...],
                ...
            }
        classes (number[]): List of classes which should be evaluated.
            Default is [0].
        difficulties (number[]): List of difficulties which should evaluated.
            Default is [0].
        min_overlap (number[]): Minimal overlap required to match bboxes.
            One entry for each class expected. Default is [0.5].
        bev (boolean): Use BEV IoU (else 3D IoU is used).
            Default is True.
        similar_classes (dict): Assign classes to similar classes that were not part of the training data so that they are not counted as false negatives.
            Default is {}.

    Returns:
        A tuple with a list of detection quantities
        (score, true pos., false. pos) for each box
        and a list of the false negatives.
    """
    ...

def sample_thresholds(scores, gt_cnt, sample_cnt=...): # -> list[Unknown]:
    """Computes equally spaced sample thresholds from given scores

    Args:
        scores (list): list of scores
        gt_cnt (number): amount of gt samples
        sample_cnt (number): amount of samples
            Default is 41.

    Returns:
        Returns a list of equally spaced samples of the input scores.
    """
    ...

def mAP(pred, target, classes=..., difficulties=..., min_overlap=..., bev=..., samples=..., similar_classes=...): # -> ndarray[Unknown, Unknown]:
    """Computes mAP of the given prediction (11-point interpolation).

    Args:
        pred (dict): List of dictionaries with the prediction data (as numpy arrays).
            {
                'bbox':       [...],
                'label':      [...],
                'score':      [...],
                'difficulty': [...]
            }[]
        target (dict): List of dictionaries with the target data (as numpy arrays).
            {
                'bbox':       [...],
                'label':      [...],
                'difficulty': [...]
            }[]
        classes (number[]): List of classes which should be evaluated.
            Default is [0].
        difficulties (number[]): List of difficulties which should evaluated.
            Default is [0].
        min_overlap (number[]): Minimal overlap required to match bboxes.
            One entry for each class expected. Default is [0.5].
        bev (boolean): Use BEV IoU (else 3D IoU is used).
            Default is True.
        samples (number): Count of used samples for mAP calculation.
            Default is 41.
        similar_classes (dict): Assign classes to similar classes that were not part of the training data so that they are not counted as false negatives.
            Default is {}.

    Returns:
        Returns the mAP for each class and difficulty specified.
    """
    ...

