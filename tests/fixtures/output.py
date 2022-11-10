STYLISH = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}''' # noqa

PLAIN = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

JSON = '''{
  "common": {
    "state": "node",
    "value": {
      "follow": {
        "state": "new",
        "value": [
          false
        ]
      },
      "setting1": {
        "state": "unchanged",
        "value": [
          "Value 1"
        ]
      },
      "setting2": {
        "state": "removed",
        "value": [
          200
        ]
      },
      "setting3": {
        "state": "changed",
        "value": [
          null,
          true
        ]
      },
      "setting4": {
        "state": "new",
        "value": [
          "blah blah"
        ]
      },
      "setting5": {
        "state": "new",
        "value": [
          {
            "key5": "value5"
          }
        ]
      },
      "setting6": {
        "state": "node",
        "value": {
          "doge": {
            "state": "node",
            "value": {
              "wow": {
                "state": "changed",
                "value": [
                  "so much",
                  ""
                ]
              }
            }
          },
          "key": {
            "state": "unchanged",
            "value": [
              "value"
            ]
          },
          "ops": {
            "state": "new",
            "value": [
              "vops"
            ]
          }
        }
      }
    }
  },
  "group1": {
    "state": "node",
    "value": {
      "baz": {
        "state": "changed",
        "value": [
          "bars",
          "bas"
        ]
      },
      "foo": {
        "state": "unchanged",
        "value": [
          "bar"
        ]
      },
      "nest": {
        "state": "changed",
        "value": [
          "str",
          {
            "key": "value"
          }
        ]
      }
    }
  },
  "group2": {
    "state": "removed",
    "value": [
      {
        "abc": 12345,
        "deep": {
          "id": 45
        }
      }
    ]
  },
  "group3": {
    "state": "new",
    "value": [
      {
        "deep": {
          "id": {
            "number": 45
          }
        },
        "fee": 100500
      }
    ]
  }
}'''
