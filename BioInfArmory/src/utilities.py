def create_dct_from_file(filename):
    """
    The file can only have two values per line.
    The first value on each line becomes the key and the second is the value.
    Keys/values remain strings.
    """
    with file(filename, 'r') as f:
        return dict(line.split() for line in f.read().strip().split('\n'))
codon_to_protein_dct = create_dct_from_file('RNA_codon_list.txt')

class FASTA_Dataset(object):
    r"""
    >>> s = ">Dataset_9000\nAGTC\nAGTC"
    >>> d = FASTA_Dataset(s)
    >>> for r in d:
    ...     print r
    ('Dataset_9000', 'AGTCAGTC')
    """
    def __init__(self, dataset):
        """
        dataset is a string with one or more data records in FASTA format
        """
        records = dataset.split('>')
        if len(records) > 1:
            records.pop(0) # empty string in well formed data set
        self.records = {}

        for record in records:
            description, data = record.split('\n', 1)
            new_record = FASTA_Record(description, data)
            self.records[str(new_record)] = new_record

    def __iter__(self):
        for data_label, record in self.records.items():
            yield (data_label, record.data)

class FASTA_Record(object):
    """
    >>> g = FASTA_Record('desc', 'data')
    >>> g.id
    >>> f = FASTA_Record('desc_0', 'data')
    >>> str(f)
    'desc_0'
    >>> f.name
    'desc'
    >>> f.id
    '0'
    >>> f.description
    ''
    >>> f.data
    'data'
    """
    def __init__(self, description, data):
        label = description.strip('>').split()
        data_id = label[0].split('_')
        self.name = data_id[0]
        self.id = None
        self.description = ''
        self.data = data.replace('\n', '')
        if len(data_id) == 2:
            self.id = data_id[1]
        if len(label) > 1:
            self.description = label[1:]
    def __str__(self):
        if self.id:
            return '_'.join([self.name, self.id])
        else:
            return self.name

if __name__ == '__main__':
    import doctest
    doctest.testmod()
