#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 03:30:29 2023

@author: malcolmlovele_snhu
"""
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD for Animal Collection"""
    
    def __init__(self, username, password):
        # Initialize MongoDB
        # Connection variables
        
        USER = 'aacuser'
        PASS = '12345'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30427
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@nv-desktop-services.apporto.com:30427/?authmechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        
        # Create method
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty\n")
        
        return False

    
    
        #R operation for R in CRUD
    def read(self, filters):
        # try/except block for testing in the unit tests
        try:
            if filters is not None:
                read_result = list(self.database.animals.find(filters, {"_id": False}))
                return read_result
            else:
                raise Exception("No filters applied")
                return False
        except Exception as e:
            print("An exception occurred: ", e)
            
    
    def update(self, filters, values):
        # Make sure data is passed 
        if filters is None:
            raise Exception("No filter specified \n")
        if values is None:
            raise Exception("No update values given\n")
            
        # Update records
        result = self.database.animals.update_many(filters, values)
        
        return result.matched_count # show number of entries updated
    
    
    def delete(self, filters):
        if filters is None:
            raise Exception("No filter specified \n")
            
        # Delete records
        result = self.database.animals.delete_many(filters)
        
        return result.deleted_count # show number of entries deleted
